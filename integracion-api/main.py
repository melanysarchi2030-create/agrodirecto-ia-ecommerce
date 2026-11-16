from fastapi import FastAPI
from pydantic import BaseModel
from odoo_connector import crear_pedido_odoo
from hubspot_sync import registrar_cliente_crm

app = FastAPI(title="AgroDirecto IA - Middleware E-Commerce", version="1.0.0")

class OrdenCompra(BaseModel):
    nombre: str
    email: str
    barrio: str
    producto: str
    total: float

@app.post("/api/v1/checkout-disruptivo")
async def procesar_compra_grupal(orden: OrdenCompra):
    # 1. Registrar pedido y descontar inventario de cosecha en Odoo ERP
    odoo_resp = crear_pedido_odoo(
        cliente=orden.nombre,
        producto=orden.producto,
        total=orden.total,
        zona=orden.barrio
    )
    
    # 2. Registrar lead y disparar campaña de fidelización en HubSpot CRM
    crm_resp = registrar_cliente_crm(
        email=orden.email,
        nombre=orden.nombre,
        barrio=orden.barrio,
        monto=orden.total
    )
    
    return {
        "estado": "APROBADO",
        "mensaje": "Sincronización End-to-End completada",
        "erp_odoo": odoo_resp,
        "crm_hubspot": crm_resp
    }
