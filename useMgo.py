import MongoDri
import json


def datetime_json_serialize(obj):
	if hasattr(obj, "isoformat"):
		return obj.isoformat()
	else:
		return obj


connection_str = "mongodb://144.173.65.33:27017"
trace_id = "f2d22892-4009-44ab-9151-3adce5ea3c87"
file_name = "trace.json"

engine = MongoDri.MongoDB(connection_str)
trace = engine.get_report(trace_id)

output = json.dumps(trace, default=datetime_json_serialize,separators=(",", ": "),indent=2)


if file_name:
	with open(file_name, "w+") as output_file:
		output_file.write(output)
else:
    print(output)