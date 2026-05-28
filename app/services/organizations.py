from uuid import uuid4

from app.core.validation import validate_required_text
from app.schemas.organizations import OrganizationCreate, OrganizationRead

_ORGANIZATIONS_BY_ID: dict[str, OrganizationRead] = {}


def create_organization(payload: OrganizationCreate) -> OrganizationRead:
    org_id = str(uuid4())
    org_name = validate_required_text(payload.name, field_name="name", max_length=100)
    org = OrganizationRead(id=org_id, name=org_name)
    _ORGANIZATIONS_BY_ID[org.id] = org

    return org


def get_organization(org_id: str) -> OrganizationRead | None:
    return _ORGANIZATIONS_BY_ID.get(org_id, None)
