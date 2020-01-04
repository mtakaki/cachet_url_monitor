#!/usr/bin/env python
"""
This file defines all the different status different values.
These are all constants and are coupled to cachet's API configuration.
"""

COMPONENT_STATUS_OPERATIONAL = 1
COMPONENT_STATUS_PERFORMANCE_ISSUES = 2
COMPONENT_STATUS_PARTIAL_OUTAGE = 3
COMPONENT_STATUS_MAJOR_OUTAGE = 4

COMPONENT_STATUSES = [COMPONENT_STATUS_OPERATIONAL,
                      COMPONENT_STATUS_PERFORMANCE_ISSUES, COMPONENT_STATUS_PARTIAL_OUTAGE,
                      COMPONENT_STATUS_MAJOR_OUTAGE]

INCIDENT_PARTIAL = 'PARTIAL'
INCIDENT_MAJOR = 'MAJOR'
INCIDENT_PERFORMANCE = 'PERFORMANCE'

INCIDENT_MAP = {
    INCIDENT_PARTIAL: COMPONENT_STATUS_PARTIAL_OUTAGE,
    INCIDENT_MAJOR: COMPONENT_STATUS_MAJOR_OUTAGE,
    INCIDENT_PERFORMANCE: COMPONENT_STATUS_PERFORMANCE_ISSUES,
}
