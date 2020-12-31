try:
    from google.cloud import firestore
except ImportError:
    raise ImportError(
        "Please ensure google-cloud-firestore version 2.0.2 is installed."
    )

import os

assert (
    "GOOGLE_APPLICATION_CREDENTIALS" in os.environ
), "Please add GOOGLE_APPLICATION_CREDENTIALS environment variable which points to service account credentials file."

from .models import Collection, Document, SubCollection
from .types import (
    Array,
    Boolean,
    GeoPoint,
    Map,
    Null,
    Number,
    Reference,
    String,
    Timestamp,
)

__version__ = "0.0.1"
