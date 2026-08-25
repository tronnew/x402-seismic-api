#!/usr/bin/env python3
"""x402 Seismic API Client — EIP-402 compliant"""
import requests, json, sys

RECIPIENT = "0x6dDCd5CC6f0614A291954daf2fF1B41DA44363DE"
PRICE = 50000
BASE_URL = "https://forex2026.mooo.com:5040"

def seismic_risk(lat, lon, radius_km=100):
    url = f"{BASE_URL}/predict"
    headers = {"Content-Type": "application/json", "X-Price": str(PRICE), "X-Recipient": RECIPIENT}
    r = requests.post(url, json={"lat": lat, "lon": lon, "radius_km": radius_km}, headers=headers)
    return r

if __name__ == "__main__":
    lat = float(sys.argv[1]) if len(sys.argv) > 1 else -33.45
    lon = float(sys.argv[2]) if len(sys.argv) > 2 else -70.67
    r = seismic_risk(lat, lon)
    print(f"Status: {r.status_code}")
    if r.status_code == 402:
        print("Payment required:", r.headers.get("X-Price"))
    else:
        print(r.text)
