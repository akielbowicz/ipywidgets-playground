Primer notebook experimentando con bqplot y pymunk.

El desarrollo de esto lo probé durante el Jupyter Workshop en Córdoba, Argentina 
durante el fin de semana del 22 y 23 de junio de 2019.

La idea era realizar poder realizar un experimento con pymunk dentro de un notebook
y que sea posible interactuar con el mismo.

La implementación obtenida es bastante hacky por un par de características de la arquitectura
tanto de bqplot y pymunk. Los cuales vuelven complicada la unión de los dos sistemas.
Por ejemplo, bqplot no tiene un objeto que tenga como traitlet las coordenadas x, y.
El objeto Mark tiene a x e y como arrays de números, por lo tanto no se pueden linkear 
las posiciones con otro widget, por ejemplo un slider.

Para remediar esto, se crearon varias funciones de callback que escuchen los cambios y modifiquen
explícitamente los otros objetos.

Para probar el notebook online [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/akielbowicz/ipywidgets-playground/master?filepath=notebooks%2Fpymunk%2Fpymunk_bqplot.ipynb)
