from .forms import UserCreationForm, AuthenticationAjaxForm


def get_context_data(request):
    return {'login_ajax': AuthenticationAjaxForm(), 'registration_form': UserCreationForm()}




