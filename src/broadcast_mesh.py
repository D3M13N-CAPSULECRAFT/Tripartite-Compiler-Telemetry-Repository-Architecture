import sqlite3, os

DB_NAME = "config/telemetry.db"

def parse_hex_to_coordinates(hex_stream):
    val = int(hex_stream[:6], 16) if len(hex_stream) >= 6 else 123456
    x = (val & 0xFF) * 0.1
    y = ((val >> 8) & 0xFF) * 0.1
    z = ((val >> 16) & 0xFF) * 0.1
    return x, y, z
