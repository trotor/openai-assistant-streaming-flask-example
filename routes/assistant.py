from flask import render_template, Blueprint, request, jsonify, Response, stream_with_context
from services.assistant_service import AssistantService

assistant_bp = Blueprint('assistant', __name__)

@assistant_bp.route('/')
def home():
    """Render the main chat interface."""
    return render_template('stream.html')

@assistant_bp.route('/assistant/name', methods=['GET'])
def get_assistant_name():
    """Get the name of the OpenAI Assistant."""
    assistant_service = AssistantService()
    assistant_name = assistant_service.assistant.name
    return jsonify({'name': assistant_name})

@assistant_bp.route('/assistant/stream', methods=['GET'])
def assistant_stream():
    """
    Stream the assistant's response to the client.
    
    Query Parameters:
        message (str): The user's input message
    
    Returns:
        Response: Server-sent events stream
    """
    message = request.args.get('message', '')
    
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    assistant_service = AssistantService()

    def generate():
        for response in assistant_service.stream_assistant(message):
            yield response

    return Response(
        stream_with_context(generate()),
        mimetype='text/event-stream',
        headers={
            'Cache-Control': 'no-cache',
            'Connection': 'keep-alive'
        }
    ) 