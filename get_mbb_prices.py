#!/usr/bin/env python3
"""
Fetch historical stock prices for MBB and save to CSV
"""

from vnstock import Quote
import pandas as pd
from datetime import datetime

# Configuration
SYMBOL = "MBB"
START_DATE = "2026-01-01"
END_DATE = "2026-02-11"
OUTPUT_FILE = f"mbb_prices_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

try:
    print(f"Fetching historical prices for {SYMBOL}...")

    # Initialize Quote API
    quote = Quote(source="kbs", symbol=SYMBOL)

    # Get historical data
    df = quote.history(
        start=START_DATE,
        end=END_DATE,
        interval="1D"  # Daily data
    )

    # Save to CSV
    df.to_csv(OUTPUT_FILE, index=False)

    # Log results
    print(f"\n✓ Successfully fetched {len(df)} records")
    print(f"✓ Saved to: {OUTPUT_FILE}")
    print(f"\nData preview:")
    print(df.head(10))
    print(f"\nData summary:")
    print(f"  Date range: {df['time'].min()} to {df['time'].max()}")
    print(f"  Price range: {df['close'].min():.2f} - {df['close'].max():.2f}")
    print(f"  Avg volume: {df['volume'].mean():,.0f}")

except Exception as e:
    print(f"✗ Error: {e}")
    print("Make sure vnstock is installed: pip install -U vnstock")