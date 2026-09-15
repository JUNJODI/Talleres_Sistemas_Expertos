
import numpy as np
from sklearn.tree import DecisionTreeClassifier, export_text


def entrenar_arbol(X: np.ndarray, Y: np.ndarray, max_depth: int = 3) -> DecisionTreeClassifier:
  
    arbol = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    arbol.fit(X, Y)
    return arbol


def extraer_reglas(arbol: DecisionTreeClassifier, nombres_variables: list[str]) -> str:
    
    return export_text(arbol, feature_names=nombres_variables)


def predecir_cliente(arbol: DecisionTreeClassifier, edad: int, horas_online: int,
                      compras_previas: int) -> tuple[int, float]:
    
    cliente = np.array([[edad, horas_online, compras_previas]])
    prediccion = int(arbol.predict(cliente)[0])
    probabilidad = float(arbol.predict_proba(cliente)[0][prediccion])
    return prediccion, probabilidad
