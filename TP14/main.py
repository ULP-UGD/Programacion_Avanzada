from gui import App
from predictor import DiabetesPredictor
from tkinter import messagebox

if __name__ == "__main__":
    try:
        MODEL_PACKAGE_PATH = 'modelo_diabetes.pkl'
        predictor = DiabetesPredictor(MODEL_PACKAGE_PATH)
        app = App(predictor)
        app.mainloop()
    except (FileNotFoundError, KeyError) as e:
        messagebox.showerror("Error Crítico de Carga", str(e))
    except Exception as e:
        messagebox.showerror(
            "Error Crítico", f"No se pudo iniciar la aplicación: {e}")