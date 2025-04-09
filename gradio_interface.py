import gradio as gr
from db import session, CaballoMovimiento, ReinaSolucion, HanoiPaso

def mostrar_caballo():
    movimientos = session.query(CaballoMovimiento).all()
    return "\n\n".join(m.recorrido for m in movimientos)

def mostrar_reinas():
    soluciones = session.query(ReinaSolucion).all()
    return "\n\n".join(r.solucion for r in soluciones)

def mostrar_hanoi():
    pasos = session.query(HanoiPaso).all()
    return "\n\n".join(p.pasos for p in pasos)

with gr.Blocks() as demo:
    gr.Markdown("# Visualizador de Juegos")

    with gr.Tab("Juego del Caballo"):
        gr.Textbox(label="Recorridos", lines=20, value=mostrar_caballo)

    with gr.Tab("8 Reinas"):
        gr.Textbox(label="Soluciones", lines=20, value=mostrar_reinas)

    with gr.Tab("Torres de Hanoi"):
        gr.Textbox(label="Pasos", lines=20, value=mostrar_hanoi)

demo.launch()