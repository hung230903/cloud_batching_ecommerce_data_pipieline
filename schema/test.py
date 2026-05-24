import pyarrow as pa


def get_ip2location_pyarrow_schema():
    """
    Define the standard PyArrow Schema for ip2location, matching BigQuery.
    """
    schema = pa.schema(
        [
            ("ip", pa.string()),
            ("country", pa.string()),
            ("region", pa.string()),
            ("city", pa.string()),
            ("latitude", pa.float64()),
            ("longitude", pa.float64()),
        ]
    )

    print(type(schema))


if __name__ == "__main__":
    get_ip2location_pyarrow_schema()
