import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self, predictor):
        super().__init__()
        self.predictor = predictor

        self.title("Predicción de Diabetes")
        self.geometry("350x450")
        self.resizable(False, False)

        self.configure(bg='#f0f0f0')
        self.font_label = ('Helvetica', 10)
        self.font_button = ('Helvetica', 12, 'bold')
        self.font_result = ('Helvetica', 14, 'bold')

        self._create_widgets()

    def _create_widgets(self):
        main_frame = tk.Frame(self, padx=20, pady=20, bg='#f0f0f0')
        main_frame.pack(fill="both", expand=True)

        labels_text = [
            "Embarazos:", "Glucosa:", "Presión Arterial:", "Grosor de Piel:",
            "Insulina:", "IMC:", "Función Pedigree:", "Edad:"
        ]

        self.entries = {}
        for i, text in enumerate(labels_text):
            label = tk.Label(main_frame, text=text,
                             font=self.font_label, bg='#f0f0f0')
            label.grid(row=i, column=0, sticky="w", pady=5, padx=5)

            entry = tk.Entry(main_frame, width=20, font=self.font_label)
            entry.grid(row=i, column=1, pady=5, padx=5)

            self.entries[text.split(":")[0]] = entry

        btn_predecir = tk.Button(
            main_frame, text="Predecir", command=self._on_predict_click,
            font=self.font_button, bg='#4CAF50', fg='white', relief='flat',
            width=15
        )
        btn_predecir.grid(row=len(labels_text), columnspan=2, pady=20)

        self.label_resultado = tk.Label(
            main_frame, text="Predicción: -", font=self.font_result,
            bg='#f0f0f0', fg='#333333'
        )
        self.label_resultado.grid(
            row=len(labels_text) + 1, columnspan=2, pady=10)

    def _on_predict_click(self):
        try:

            input_data = [float(entry.get())
                          for entry in self.entries.values()]

            resultado = self.predictor.make_prediction(input_data)

            self.label_resultado.config(text=resultado)

            if "Sí" in resultado:
                self.label_resultado.config(fg='red')
            else:
                self.label_resultado.config(fg='green')

        except ValueError:
            messagebox.showerror(
                "Error de Entrada", "Por favor, ingresa solo valores numéricos válidos en todos los campos.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error inesperado: {e}")