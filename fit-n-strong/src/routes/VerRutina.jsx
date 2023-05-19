import { React, useEffect, useState, setState } from "react";
import { Button, Table, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import AgregarEjercicio from "./AgregarEjercicio";
import EditarEjercicio from "./EditarEjercicio";
import EliminarEjercicio from "./EliminarEjercicio";

import axios from "axios";
import { useParams } from "react-router-dom";

export default function VerRutina() {

    const {id} = useParams();

    const [modalNew, setModalNew] = useState(false);
    const [modalEdit, setModalEdit] = useState(false);
    const [modalDelete, setModalDelete] = useState(false);

    const [modalEditId, setModalEditId] = useState(0);
    const [modalDeleteId, setModalDeleteId] = useState(0);
  
    const toggleNew = () => setModalNew(!modalNew);
    const toggleEdit = () => setModalEdit(!modalEdit);
    const toggleDelete = () => setModalDelete(!modalDelete)

    const [exercises, setExercises] = useState([]);
    const [routine, setRoutine] = useState({nombre: ''});

    // traer ejercicios de la rutina seleccionada
    useEffect(() => {
        getRoutine();
        getExercises();
    }, []);
    
    function getRoutine() {
        axios.get('http://20.226.52.146:8080/rutina?id=' + id, {
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => response.data)
        .then(data => setRoutine({nombre: data.nombre}))
        .catch(error => {
            console.log("Hubo un error al intentar obtener las rutinas", error);
        });
    }

    function getExercises() {
        axios.get('http://20.226.52.146:8080/ejercicios?id=' + id, {
            headers: {
                "Content-Type": "application/json",
            },
        })
        .then(response => response.data)
        .then(data => setExercises([...Object.values(data)]))
        .catch(error => {
            console.log("Hubo un error al intentar obtener las rutinas", error);
        });
    }

    return (
        <div className="container">
            <h2 className="title">Rutina {routine.nombre}</h2>

            <div className="add-btn-container">
                <Button onClick={toggleNew} className='add-button' color="success">
                    <AddIcon /> Agregar Ejercicio
                </Button>
            </div>
            <Modal isOpen={modalNew} fade={false} toggle={toggleNew}>
                <ModalHeader toggle={toggleNew}>Agregar Ejercicio</ModalHeader>
                <ModalBody>
                    <AgregarEjercicio toggle={toggleNew} getExercises={getExercises} routineId={id} />
                </ModalBody>
            </Modal>

            <Table dark>
                <thead>
                    <tr>
                    <th>Nombre Ejercicio</th>
                    <th>Repeticiones</th>
                    <th>Duración</th>
                    <th>Peso </th>
                    <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {exercises.map((exercise, index) => {
                        return <tr key={index}>
                            <th>{exercise.nombre}</th>
                            <td>{exercise.repeticiones}</td>
                            <td>{exercise.duracion}</td>
                            <td>{exercise.peso}</td>
                            <td className='actions'>
                                <Button onClick={() => {toggleEdit(); setModalEditId(exercise.ejercicio_id)}} color="warning">
                                    <EditIcon /> Editar
                                </Button>
                                <Modal isOpen={modalEditId === exercise.ejercicio_id && modalEdit} fade={false} toggle={toggleEdit}>
                                    <ModalHeader toggle={toggleEdit}>Editar Ejercicio</ModalHeader>
                                    <ModalBody>
                                        <EditarEjercicio id={exercise.ejercicio_id} toggle={toggleEdit} getExercises={getExercises} />
                                    </ModalBody>
                                </Modal>

                                <Button onClick={() => {toggleDelete(); setModalDeleteId(exercise.ejercicio_id)}} color="danger">
                                    <DeleteIcon /> Eliminar
                                </Button>
                                <Modal isOpen={modalDeleteId === exercise.ejercicio_id && modalDelete} fade={false} 
                                    toggle={toggleDelete}>

                                    <ModalHeader toggle={toggleDelete}>Eliminar Ejercicio</ModalHeader>
                                    <ModalBody>
                                        <EliminarEjercicio id={exercise.ejercicio_id} toggle={toggleDelete} getExercises={getExercises} />
                                    </ModalBody>
                                </Modal>
                            </td>
                        </tr>
                    }) }
                </tbody>
            </Table>
        </div>
    );
}