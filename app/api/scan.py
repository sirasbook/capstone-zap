from fastapi import APIRouter, Body, Response
from app.schemas import Zap_input
from starlette.responses import JSONResponse
import logging, os, json

router = APIRouter()
REPORT_FOLDER = '/zap/wrk/app/reports'

def load_json():
    f = open(REPORT_FOLDER + '/zap-report.json')
    data = json.load(f)
    return data

def clear_reports():
    for file_name in os.listdir(REPORT_FOLDER):
        file_path = os.path.join(REPORT_FOLDER, file_name)
        try:
            os.unlink(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

@router.post("/basescan", status_code=200)
def basescan(req_body: Zap_input = Body(...)) -> Response:
    try:
        if req_body:
            url = req_body.url
            clear_reports()
            os.system(f'/bin/sh -c "app/zap/start-baseline.sh {url}"')

            data = load_json()
            result = {
                "alerts": []
            }

            for obj in data['alerts']:
                result['alerts'].append(obj)

            return JSONResponse(
                status_code = 200,
                content = result
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
            clear_reports()
            os.system(f'/bin/sh -c "app/zap/start-fullscan.sh {url}"')

            data = load_json()
            result = {
                "alerts": []
            }

            for obj in data['alerts']:
                result['alerts'].append(obj)

            return JSONResponse(
                status_code = 200,
                content = result
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
