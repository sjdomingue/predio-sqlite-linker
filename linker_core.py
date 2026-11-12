# -*- coding: utf-8 -*-
"""
Generic Parcel-SQLite Linker for QGIS
A portfolio version demonstrating PyQGIS and SQLite integration.
"""

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QAction, QDockWidget, QMessageBox
from qgis.core import QgsProject, QgsVectorLayer
import sqlite3
import os

# Configuración genérica (Sin datos reales)
MUNICIPIOS_EJEMPLO = ["CIUDAD_PRUEBA", "MUNICIPIO_DEMO"]
COLUMNAS_RELEVANTES = ["ID_PREDIO", "DIRECCION", "ESTADO"]

class GenericLinkerPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        # Base de datos ficticia en una carpeta local, NO en OneDrive corporativo
        self.db_path = os.path.join(self.plugin_dir, "data", "sample_database.sqlite")
        self.action = None

    def initGui(self):
        self.action = QAction("Parcel SQLite Linker (Demo)", self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Demo Plugins", self.action)

    def unload(self):
        self.iface.removePluginMenu("&Demo Plugins", self.action)
        self.iface.removeToolBarIcon(self.action)

    def run(self):
        # Demostración de conexión a SQLite de forma segura
        if not os.path.exists(self.db_path):
            QMessageBox.warning(None, "Demo", "Base de datos de ejemplo no encontrada.")
            return
            
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tablas = cursor.fetchall()
            conn.close()
            
            # Lógica para vincular predios aquí (simulada para el portafolio)
            QMessageBox.information(None, "Éxito", f"Conexión exitosa. Tablas disponibles: {len(tablas)}")
            
        except Exception as e:
            QMessageBox.critical(None, "Error", f"Error de conexión: {str(e)}")