from ai_integration.public_interface import start_loop

from model import initialize, infer

initialize()

start_loop(inference_function=infer, inputs_schema={
    "text": {
        "type": "text"
    }
})
