
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def test_product_catalogue_exists():
    assert (ROOT / "products.csv").exists()


def test_product_catalogue_has_required_columns():
    products = pd.read_csv(ROOT / "products.csv")

    required = {
        "id",
        "name",
        "category",
        "brand",
        "price_inr",
        "rating",
        "features",
        "specifications",
        "best_for",
        "available",
        "product_url",
    }

    assert required.issubset(set(products.columns))
    assert len(products) > 0
