from http import HTTPStatus

import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3 import Retry


def requests_retry(
    retries=3,
    back_off_factor=0.3,
    status_force_list=(
        HTTPStatus.BAD_GATEWAY,
        HTTPStatus.SERVICE_UNAVAILABLE,
        HTTPStatus.GATEWAY_TIMEOUT,
        HTTPStatus.REQUEST_TIMEOUT,
    ),
    session=None,
) -> Session:
    session = session or requests.Session()
    adapter = HTTPAdapter(
        max_retries=Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=back_off_factor,
            status_forcelist=status_force_list,
            method_whitelist=False,
        )
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
