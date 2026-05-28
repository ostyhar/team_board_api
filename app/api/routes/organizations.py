from fastapi import APIRouter, HTTPException, status

from app.schemas.organizations import OrganizationCreate, OrganizationRead
from app.services.organizations import create_organization, get_organization

router = APIRouter(prefix="/organizations", tags=["organizations"])


@router.post("", response_model=OrganizationRead, status_code=status.HTTP_201_CREATED)
def create_organization_endpoint(payload: OrganizationCreate) -> OrganizationRead:
    try:
        org = create_organization(payload)
    except ValueError as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(ex),
        ) from ex

    return org


@router.get(
    "/{org_id}", response_model=OrganizationRead, status_code=status.HTTP_200_OK
)
def get_organization_endpoint(org_id: str) -> OrganizationRead:
    org = get_organization(org_id)

    if org is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Organization with id: {org_id} not found",
        )

    return org
