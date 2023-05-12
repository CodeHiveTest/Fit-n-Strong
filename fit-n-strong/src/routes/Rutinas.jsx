import { React, useState } from "react";
import { Button, Table, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import EditIcon from '@mui/icons-material/Edit';
import RemoveRedEyeIcon from '@mui/icons-material/RemoveRedEye';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import { Link } from 'react-router-dom';
import "./../styles/Rutinas.css";
import NuevaRutina from "./NuevaRutina";
import EditarRutina from "./EditarRutina";

export default function Rutinas() {
    const [modalNew, setModalNew] = useState(false);
    const [modalEdit, setModalEdit] = useState(false);
    const [modalDelete, setModalDelete] = useState(false);
  
    const toggleNew = () => setModalNew(!modalNew);
    const toggleEdit = () => setModalEdit(!modalEdit);
    const toggleDelete = () => setModalDelete(!modalDelete);

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
                    <NuevaRutina props={{toggleNew}} />
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
                    <tr>
                        <th>ID</th>
                        <td>First Name</td>
                        <td className='actions'>
                            <Link to='/ver-rutina'>
                                <Button color="success">
                                <RemoveRedEyeIcon /> Ver
                                </Button>
                            </Link>

                            <Button onClick={toggleEdit} color="warning">
                                <EditIcon /> Editar
                            </Button>
                            <Modal isOpen={modalEdit} fade={false} toggle={toggleEdit}>
                                <ModalHeader toggle={toggleEdit}>Editar Rutina</ModalHeader>
                                <ModalBody>
                                    <EditarRutina props={{toggleDelete}} />
                                </ModalBody>
                            </Modal>

                            <Button onClick={toggleDelete} color="danger">
                                <DeleteIcon /> Eliminar
                            </Button>
                            <Modal isOpen={modalDelete} fade={false} toggle={toggleDelete}>
                                <ModalHeader toggle={toggleDelete}>Eliminar Rutina</ModalHeader>
                                <ModalBody>
                                ¿Está seguro que desea eliminar esta rutina? Esta acción no se puede deshacer...
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
                </tbody>
            </Table>
        </div>
    );
}