# Christmas Control Panel
<img width="1279" height="580" alt="image" src="https://github.com/user-attachments/assets/cc1a4912-ff9f-4c82-91f5-a8bb0e62bb8a" />

# 🎄 Christmas Control Panel
Un panel de control para PC con un estilo navideño moderno, creado especialmente para la temporada. Su objetivo es ofrecer herramientas simples, rápidas y útiles dentro de una interfaz festiva y agradable.

Actualmente el proyecto está en desarrollo activo y se irán añadiendo nuevas funciones con el tiempo.

---

## ✨ Características actuales

### ✅ *System Info*

| <img width="1291" height="634" alt="image" src="https://github.com/user-attachments/assets/3ea5d473-7ffe-4c07-bdc0-510d8784733f" /> |
|---|


Muestra información básica del sistema, como:
- Nombre del dispositivo
- Sistema operativo
- Arquitectura
- RAM disponible
- Otros datos relevantes según la plataforma

### ✅ *IP Geolocate*

| <img width="1161" height="615" alt="image" src="https://github.com/user-attachments/assets/593b2ed7-9058-4677-912d-cf73a6b8b077" /> |
|---|


Permite obtener la geolocalización aproximada de una dirección IP:
- País
- Ciudad
- Región
- ISP (si está disponible)
- Coordenadas aproximadas

### ✅ *Run Port*

| <img width="1000" height="600" alt="image" src="https://github.com/user-attachments/assets/6fa5c8fb-4b54-41f0-a88c-de72547f16fc" /> | <img width="1000" height="45" alt="image" src="https://github.com/user-attachments/assets/94e9a2e2-939c-4801-98cf-2e0852361c63" /> |
|---|---|

Permite abrir un puerto local en una carpeta o archivo de la PC:
- Introduce numero de Puerto
- Introduce ubicacion del archivo a mostrar
- Abre el puerto en localhost

### ✅ *My Public IP*
| <img width="1184" height="391" alt="image" src="https://github.com/user-attachments/assets/c48e198a-91af-4155-8c39-0c2ea5a3d5db" /> |
|---|

Muestra tu IP publica en formato de texto

---

## 🎅 Estilo navideño
El panel utiliza una interfaz inspirada en la estética navideña:
- Colores cálidos y festivos
- Animaciones suaves
- Elementos decorativos sutiles
- Diseño minimalista tipo “Google UI”

Perfecto para lanzar durante las fiestas.

---

## 🛠 Estado del proyecto
El proyecto *está en desarrollo*.  
Próximas funciones planificadas:
- Monitor de rendimiento (CPU, RAM, disco)
- Información de red en tiempo real
- Herramientas de diagnóstico
- Módulos adicionales según feedback

---

## 📦 Instalacion y Uso
Descargue el ZIP del repo desde la seccion Code>Download

  ir a la carpeta del proyecto ```cd "C:/Users/Tu-Usuario/Downloads/ControlPanel-LocalWeb-master"```
  
  instalar requirements.txt ```pip install -r requirements.txt```
  
  correr la api ```python -m uvicorn main:app --reload```
  
  entrar a la web: ir en el navegador a ```127.0.0.1:8000```
