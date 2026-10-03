#!/usr/bin/env python3
import wp2b_fetch_v2 as base

# WP2B policy: DCOILWTICO remains excluded from the versioned panel until
# redistribution/provenance treatment is resolved under Q034.
base.SER.pop("DCOILWTICO", None)

if __name__ == "__main__":
    base.main()
