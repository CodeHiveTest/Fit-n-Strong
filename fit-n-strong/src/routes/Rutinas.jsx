import { React, useEffect, useState } from "react";
import { Button, Table, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import EditIcon from '@mui/icons-material/Edit';
import RemoveRedEyeIcon from '@mui/icons-material/RemoveRedEye';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import { useNavigate, redirect } from 'react-router-dom';
import "./../styles/Rutinas.css";
import NuevaRutina from "./NuevaRutina";
import EditarRutina from "./EditarRutina";
import EliminarRutina from "./EliminarRutina";
import axios from "axios";

export default function Rutinas() {
    const [modalNew, setModalNew] = useState(false);
    const [modalEdit, setModalEdit] = useState(false);
    const [modalDelete, setModalDelete] = useState(false);

    const [modalEditId, setModalEditId] = useState(0);
    const [modalDeleteId, setModalDeleteId] = useState(0);
  
    const toggleNew = () => setModalNew(!modalNew);
    const toggleEdit = () => setModalEdit(!modalEdit);
    const toggleDelete = () => setModalDelete(!modalDelete)

    const [routines, setRoutines] = useState([]);

    const navigate = useNavigate();

    // traer rutinas creadas por el usuario de la API
    useEffect(() => {
        getRoutines();
    }, []);

    useEffect(() => {
        console.log(routines);
    }, [routines]);

    function getRoutines() {
        axios.get('http://20.226.52.146:8080/rutinas', {
            headers: {
            "Content-Type": "application/json",
            },
        })
        .then(response => response.data)
        .then(data => setRoutines([...Object.values(data)]))
        .catch(error => {
            console.log("Hubo un error al intentar obtener las rutinas", error);
        });
    }

    const handleVerRutina = (id) => {
        navigate('/ver-rutina/' + id);
    };

    return (
        <div className='container'>

            <h2 className="title">Mis Rutinas</h2>
            
            <div className="add-btn-container">
                <Button onClick={toggleNew} className='add-button' color="success">
                    <AddIcon /> Nueva Rutina
                </Button>
            </div>
            <Modal isOpen={modalNew} fade={false} toggle={toggleNew}>
                <ModalHeader toggle={toggleNew}>Crear Rutina</ModalHeader>
                <ModalBody>
                    <NuevaRutina toggle={toggleNew} getRoutines={getRoutines} />
                </ModalBody>
            </Modal>

            <Table dark>
                <thead>
                    <tr>
                    <th>Nombre Rutina</th>
                    <th>Grupo Muscular</th>
                    <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {routines.map((routine, index) => {
                        return <tr key={index}>
                            <th>{routine.nombre}</th>
                            <td>{routine.grupo_muscular}</td>
                            <td className='actions'>
                                <Button color="success" onClick={() => handleVerRutina(routine.id)}>
                                    <RemoveRedEyeIcon /> Ver
                                </Button>

                                <Button onClick={() => {toggleEdit(); setModalEditId(routine.id)}} color="warning">
                                    <EditIcon /> Editar
                                </Button>

                                <Modal key={routine.id} isOpen={modalEditId === routine.id && modalEdit} fade={false} 
                                    toggle={toggleEdit}>

                                    <ModalHeader toggle={toggleEdit}>Editar Rutina</ModalHeader>
                                    <ModalBody>
                                        <EditarRutina id={routine.id} toggle={toggleEdit} getRoutines={getRoutines} />
                                    </ModalBody>

                                </Modal>

                                <Button onClick={() => {toggleDelete(); setModalDeleteId(routine.id)}} color="danger">
                                    <DeleteIcon /> Eliminar
                                </Button>
                                <Modal isOpen={modalDeleteId === routine.id && modalDelete} fade={false} toggle={toggleDelete}>
                                    <ModalHeader toggle={toggleDelete}>Eliminar Rutina</ModalHeader>
                                    <ModalBody>
                                        <EliminarRutina id={routine.id} toggle={toggleDelete} getRoutines={getRoutines} />
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