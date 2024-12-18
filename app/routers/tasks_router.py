from fastapi import APIRouter, HTTPException, Query, Path, status
from models import Task, UpdateTaskModel, TaskList
from app.db import db

tasks_router = APIRouter()

"""
Task Router Module

Este módulo implementa los endpoints para la gestión de tareas en la API.
Proporciona operaciones CRUD completas para el manejo de tareas.

Endpoints disponibles:
    POST /tasks/ : Crea una nueva tarea
    GET /tasks/ : Obtiene lista de todas las tareas
    GET /tasks/{task_id} : Obtiene una tarea específica
    PUT /tasks/{task_id} : Actualiza una tarea existente
    DELETE /tasks/{task_id} : Elimina una tarea específica
    DELETE /tasks/all : Elimina todas las tareas

Modelos utilizados:
    - Task: Modelo completo de una tarea
    - UpdateTaskModel: Modelo para actualización parcial de tareas
    - TaskList: Modelo para lista de tareas
"""

@tasks_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task):
    """
    Crea una nueva tarea.
    
    Args:
        task (Task): Datos de la tarea a crear
    
    Returns:
        Task: Tarea creada con ID asignado
    """

@tasks_router.get("/{task_id}")
async def get_task(task_id: int = Path(..., gt=0)):
    """
    Obtiene una tarea específica por su ID.
    
    Args:
        task_id (int): ID de la tarea a buscar
    
    Returns:
        Task: Datos de la tarea encontrada
        
    Raises:
        HTTPException: 404 si la tarea no existe
    """

@tasks_router.get("/", response_model=TaskList)
async def get_tasks():
    """
    Obtiene todas las tareas existentes.
    
    Returns:
        TaskList: Lista con todas las tareas
    """

@tasks_router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: UpdateTaskModel):
    """
    Actualiza una tarea existente.
    
    Args:
        task_id (int): ID de la tarea a actualizar
        task_update (UpdateTaskModel): Datos a actualizar
    
    Returns:
        Task: Tarea actualizada
        
    Raises:
        HTTPException: 404 si la tarea no existe
    """

@tasks_router.delete("/all")
async def delete_all_tasks():
    """
    Elimina todas las tareas de la base de datos.
    
    Returns:
        dict: Mensaje de confirmación
    """

@tasks_router.delete("/{task_id}")
async def delete_task(task_id: int):
    """
    Elimina una tarea específica.
    
    Args:
        task_id (int): ID de la tarea a eliminar
    
    Returns:
        dict: Mensaje de confirmación
    """
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
