"""Вход через внешних провайдеров (в разработке)."""

PROVIDERS = ("google", "apple")


def build_authorize_url(provider, client_id, redirect_uri):
    if provider not in PROVIDERS:
        raise ValueError(f"unknown provider: {provider}")
    return (
        f"https://auth.{provider}.com/authorize"
        f"?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
    )


def exchange_code_for_token(provider, code):
    # TODO: реальный обмен кода на токен
    raise NotImplementedError
