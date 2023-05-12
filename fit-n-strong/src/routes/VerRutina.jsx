import { React, useState } from "react";
import { Button, Table, Modal, ModalHeader, ModalBody, ModalFooter } from 'reactstrap';
import EditIcon from '@mui/icons-material/Edit';
import RemoveRedEyeIcon from '@mui/icons-material/RemoveRedEye';
import DeleteIcon from '@mui/icons-material/Delete';
import AddIcon from '@mui/icons-material/Add';
import AgregarEjercicio from "./AgregarEjercicio";
import EditarEjercicio from "./EditarEjercicio";

export default function VerRutina() {

    const [modalNew, setModalNew] = useState(false);
    const [modalEdit, setModalEdit] = useState(false);
    const [modalDelete, setModalDelete] = useState(false);
  
    const toggleNew = () => setModalNew(!modalNew);
    const toggleEdit = () => setModalEdit(!modalEdit);
    const toggleDelete = () => setModalDelete(!modalDelete);

    return (
        <div className="container">
            <h2 className="title">Rutina 'Nombre Rutina'</h2>

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
                    <th>Peso</th>
                    <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <th>ID</th>
                        <td>First Name</td>
                        <td>Last Name</td>
                        <td>Username</td>
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
                </tbody>
            </Table>
        </div>
    );
}