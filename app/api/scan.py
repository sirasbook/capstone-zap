from fastapi import APIRouter, Body, Response
from app.schemas import Zap_input
from starlette.responses import JSONResponse
import logging, os, json

router = APIRouter()

@router.post("/basescan", status_code=200)
def basescan(req_body: Zap_input = Body(...)) -> Response:
    try:
        if req_body:
            url = req_body.url
            os.system(f'/bin/sh -c "app/zap/start-baseline.sh {url}"')

            return JSONResponse(
                status_code = 200,
                content = {
                    "message": "Success",
                },
            )
        else:
            return JSONResponse(
                status_code = 400,
                content = {
                    "message": "Invalid Request"
                }
            )
    except Exception as e:
        logging.error(e)
        return JSONResponse(
            status_code = 400,
            content = {
                "message": "error"
            }
        )

@router.post("/fullscan", status_code=200)
def fullscan(req_body: Zap_input = Body(...)) -> Response:
    try:
        if req_body:
            url = req_body.url
            os.system(f'/bin/sh -c "app/zap/start-fullscan.sh {url}"')
            return JSONResponse(
                status_code = 200,
                content = {
                    "message": "Success",
                },
            )
        else:
            return JSONResponse(
                status_code = 400,
                content = {
                    "message": "Invalid Request"
                }
            )
    except Exception as e:
        logging.error(e)
        return JSONResponse(
            status_code = 400,
            content = {
                "message": "error"
            }
        )
