from flask import Flask, request, jsonify
from orm.setting import session
from orm.model import Data
from datetime import datetime
from marshmallow import Schema, fields, EXCLUDE, ValidationError
import traceback

app = Flask(__name__)


class DataSchema(Schema):
    source = fields.String(required=True)
    date = fields.DateTime(required=True)
    temperature = fields.Decimal(as_string=True, places=2)
    humid = fields.Decimal(as_string=True, places=2)
    data1 = fields.Decimal(as_string=True, places=2)
    data2 = fields.Decimal(as_string=True, places=2)
    data3 = fields.Boolean()

class DataListSchema(Schema):
    data_list = fields.List(fields.Nested(DataSchema), required=True)

@app.route('/register', methods=['POST'])
def register():
    try:
        schema = DataListSchema()

        result = schema.load(request.get_json())
        app.logger.info(result)

        session.bulk_insert_mappings(Data, result['data_list'])
        session.commit()

        return jsonify({"status": "success", "yourData": request.get_json()}), 200

    except ValidationError as e:
        trace = traceback.format_exc()
        app.logger.warning(f'Error!: {e}\n{trace}')
        return jsonify(e.messages), 400
    except Exception as e:
        trace = traceback.format_exc()
        app.logger.warning(f'Error!: {e}\n{trace}')
        return jsonify(str(e)+'trace:'+trace), 500

@app.route('/')
def hello():
    return 'hello', 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8081, use_reloader=False)