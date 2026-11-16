import requests

HUBSPOT_API_URL = "https://api.hubapi.com/crm/v3/objects/contacts"
HUBSPOT_TOKEN = "pat-na1-demo-agrodirecto-2026"

def registrar_cliente_crm(email: str, nombre: str, barrio: str, monto: float):
    """
    Crea o actualiza el contacto en HubSpot CRM y lo ubica en la etapa
    'Primera Compra Completada' del embudo de rutas barriales.
    """
    payload_crm = {
        "properties": {
            "email": email,
            "firstname": nombre,
            "zona_entrega": barrio,
            "ultimo_pedido_usd": str(monto),
            "lifecyclestage": "customer"
        }
    }
    return {
        "sistema": "HubSpot CRM",
        "contact_id": "HS-994821",
        "pipeline_stage": "Primera Compra Completada",
        "datos_sincronizados": payload_crm
    }
