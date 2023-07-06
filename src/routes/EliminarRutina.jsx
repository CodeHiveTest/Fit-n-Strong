import React, { useState, useEffect } from 'react';
import { Button, Form, FormGroup, Label, Col, Input } from 'reactstrap';
import axios from "axios";

export default function EliminarRutina({id, toggle, getRoutines}) {

    useEffect(() => {
        getRoutines();
    }, []);

    // hacer llamada a la API para obtener los datos de la rutina que se está modificando
    function submit(event) {
        event.preventDefault();
        axios.delete('http://20.226.52.146:8080/rutinas?id=' + id, {
            headers: {
                "Content-Type": "text/plain",
            },
        })
        .then(AxiosResponse => {
            if(AxiosResponse.status == 200) {
                getRoutines();
            }
        })
        .catch(error => {
            getRoutines();
            //alert("Ocurrió el siguiente error al tratar de crear la rutina:", error);
        });

        toggle();
    }

    return (
        <Form onSubmit={submit}>
            <FormGroup row>
                ¿Está seguro que desea eliminar esta rutina? Esta acción no se puede deshacer...
            </FormGroup>
            <FormGroup check row>
                <Col sm={{ offset: 2, size: 10 }}>
                <Button color="danger" type="submit">
                    Eliminar
                </Button>{' '}
                <Button color="secondary" onClick={toggle}>
                    Cancelar
                </Button>
                </Col>
            </FormGroup>
        </Form>
    );
}
