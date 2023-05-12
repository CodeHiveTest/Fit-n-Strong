import { React, useEffect, useState, setState } from "react";
import { Button, Table, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import EditIcon from '@mui/icons-material/Edit';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import AgregarEjercicio from "./AgregarEjercicio";
import EditarEjercicio from "./EditarEjercicio";

import axios from "axios";

export default function VerRutinatry() {

    const [modalNew, setModalNew] = useState(false);
    const [modalEdit, setModalEdit] = useState(false);
    const [modalDelete, setModalDelete] = useState(false);
  
    const toggleNew = () => setModalNew(!modalNew);
    const toggleEdit = () => setModalEdit(!modalEdit);
    const toggleDelete = () => setModalDelete(!modalDelete);

    const [exercises, setExercises] = useState([]);

    // traer ejercicios de la rutina seleccionada
    useEffect(() => {
        getExercises();
    }, []);

    function getExercises() {
        axios.get('http://20.226.52.146:8080/ejercicios?rut_id=1', {
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
            <h2 className="title">Rutina 'brazos'</h2>

            <div className="add-btn-container">
                <Button onClick={toggleNew} className='add-button' color="success">
                    <AddIcon /> Agregar Ejercicio
                </Button>
            </div>
            <Modal isOpen={modalNew} fade={false} toggle={toggleNew}>
                <ModalHeader toggle={toggleNew}>Agregar Ejercicio</ModalHeader>
                <ModalBody>
                    <AgregarEjercicio props={{toggleNew}} />
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
                                <Button onClick={toggleEdit} color="warning">
                                    <EditIcon /> Editar
                                </Button>
                                <Modal isOpen={modalEdit} fade={false} toggle={toggleEdit}>
                                    <ModalHeader toggle={toggleEdit}>Editar Ejercicio</ModalHeader>
                                    <ModalBody>
                                        <EditarEjercicio props={{toggleDelete}} />
                                    </ModalBody>
                                </Modal>

                                <Button onClick={toggleDelete} color="danger">
                                    <DeleteIcon /> Eliminar
                                </Button>
                                <Modal isOpen={modalDelete} fade={false} toggle={toggleDelete}>
                                    <ModalHeader toggle={toggleDelete}>Eliminar Ejercicio</ModalHeader>
                                    <ModalBody>
                                    ¿Está seguro que desea eliminar este ejercicio de la rutina? Esta acción no se puede deshacer...
                                    </ModalBody>
                                    <ModalFooter>
                                    <Button color="danger" onClick={toggleDelete}>
                                        Eliminar
                                    </Button>{' '}
                                    <Button color="secondary" onClick={toggleDelete}>
                                        Cancelar
                                    </Button>
                                    </ModalFooter>
                                </Modal>
                            </td>
                        </tr>
                    }) }
                </tbody>
            </Table>
        </div>
    );
}