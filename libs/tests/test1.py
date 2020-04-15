from medium import Client
client=Client(application_id="bd2220b27e6a",application_secret="5ea5ccec18e6b7d12466900d47417fdcc52f352f")
client.access_token ="2a0432ffe8985834d0f939991291b6d589eef0684b425e8fce1c964a7e0be1263" 
user=client.get_current_user()
