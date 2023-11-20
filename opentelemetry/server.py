# pip install opentelemetry-api
# pip install opentelemetry-sdk
# pip install opentelemetry-distro
# opentelemetry-bootstrap -a install
# Run with: opentelemetry-instrument --traces_exporter console --metrics_exporter console flask --app server run
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter

name = "test"

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)
tracer = trace.get_tracer(name)

app = Flask(name)
 
@app.route('/')
def index():
  with tracer.start_as_current_span("server_request"):
    return 'Hello World!'
 
app.run(host='0.0.0.0', port=8000)