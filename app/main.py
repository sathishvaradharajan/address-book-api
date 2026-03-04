from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
import logging

from .database import Base, engine, get_db
from . import models, schemas, crud
from .utils import calculate_distance


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI(title="Address Book API")

Base.metadata.create_all(bind=engine)


@app.post(
    "/addresses",
    response_model=schemas.AddressResponse,
    status_code=status.HTTP_201_CREATED
)
def create_address(
    address: schemas.AddressCreate,
    db: Session = Depends(get_db)
):

    logger.info("Create address request received")

    try:
        new_address = crud.create_address(db, address)
        logger.info(f"Address created with id {new_address.id}")
        return new_address

    except Exception as e:
        logger.error(f"Failed to create address: {e}")
        raise HTTPException(
            status_code=500,
            detail="Failed to create address"
        )


@app.put("/addresses/{address_id}", response_model=schemas.AddressResponse)
def update_address(
    address_id: int,
    address: schemas.AddressUpdate,
    db: Session = Depends(get_db)
):

    logger.info(f"Update request for address {address_id}")

    db_address = crud.update_address(db, address_id, address)

    if not db_address:
        logger.warning(f"Address {address_id} not found for update")
        raise HTTPException(status_code=404, detail="Address not found")

    logger.info(f"Address {address_id} updated")

    return db_address


@app.delete("/addresses/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_address(
    address_id: int,
    db: Session = Depends(get_db)
):

    logger.info(f"Delete request for address {address_id}")

    db_address = crud.delete_address(db, address_id)

    if not db_address:
        logger.warning(f"Address {address_id} not found for deletion")
        raise HTTPException(status_code=404, detail="Address not found")

    logger.info(f"Address {address_id} deleted")


@app.get("/addresses/nearby")
def nearby_addresses(
    lat: float,
    lon: float,
    distance_km: float,
    db: Session = Depends(get_db)
):

    logger.info(
        f"Nearby search requested for ({lat}, {lon}) within {distance_km} km"
    )

    addresses = crud.get_all_addresses(db)

    result = []

    for addr in addresses:

        distance = calculate_distance(
            lat,
            lon,
            addr.latitude,
            addr.longitude
        )

        if distance <= distance_km:
            result.append(addr)

    logger.info(f"{len(result)} addresses found within distance")

    return result