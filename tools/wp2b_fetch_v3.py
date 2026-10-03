#!/usr/bin/env python3
import wp2b_fetch_v2 as base

# WP2B policy: raw alternative/stress series with unresolved redistribution
# treatment stay out of the public versioned panel until Q034 is resolved.
base.SER.pop("DCOILWTICO", None)
base.SER.pop("STLFSI4", None)

if __name__ == "__main__":
    base.main()
