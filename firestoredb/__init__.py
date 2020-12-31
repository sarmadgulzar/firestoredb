try:
    from google.cloud import firestore
except ImportError:
    raise ImportError("Please ensure google-cloud-firestore version 2.0.2 is installed.")

from types import (
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

__version__ = '0.0.1'
