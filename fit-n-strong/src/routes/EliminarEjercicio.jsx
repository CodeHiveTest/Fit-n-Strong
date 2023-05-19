import React, { useState, useEffect } from 'react';
import { Button, Form, FormGroup, Label, Col, Input } from 'reactstrap';
import axios from "axios";

export default function EliminarRutina({id, toggle, getExercises}) {

    useEffect(() => {
        getExercises();
    }, []);

    // hacer llamada a la API para obtener los datos de la rutina que se está modificando
    function submit(event) {
        event.preventDefault();
        axios.delete('http://20.226.52.146:8080/ejercicios?id=' + id, {
            headers: {
                "Content-Type": "text/plain",
            },
        })
        .then(response => {
            if(response.status === 200) {
                getExercises();
            }
        })
        .catch(error => {
            alert("Ocurrió el siguiente error al tratar de crear un nuevo ejercicio:", error);
        });

        toggle();
    }

    return (
        <Form onSubmit={submit}>
            <FormGroup row>
                ¿Está seguro que desea eliminar este ejercicio de la rutina? Esta acción no se puede deshacer...
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
