from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_items():
    return [{"id": 1, "name": "item-1"}, {"id": 2, "name": "item-2"}]


@router.get("/{item_id}")
def get_item(item_id: int):
    return {"id": item_id, "name": f"item-{item_id}"}
