import React, { useState, useEffect } from 'react';
import { Button, Form, FormGroup, Label, Col, Input } from 'reactstrap';
import axios from "axios";

export default function EditarRutina({toggle, getRoutines}) {

    const [routineName, setRoutineName] = useState('');
    const [grupo, setGrupo] = useState('');

    useEffect(() => {
        getRoutines();
    }, []);

    // hacer llamada a la API para obtener los datos de la rutina que se está modificando
    function submit(event) {
        event.preventDefault();
        console.log("Se mandó");
        console.log(routineName, " - ", grupo);
        axios.put('http://20.226.52.146:8080/rutinas', {
            headers: {
                "Content-Type": "text/plain",
            },
            rutina_id: routineName,
            nombre: routineName,
            grupo_muscular: grupo
        })
        .then(response => response.data)
        .then(data => {
            if(data.status === 201) {
                getRoutines();
            }
        })
        .catch(error => {
            alert("Ocurrió el siguiente error al tratar de crear la rutina:", error);
        });

        toggle();
    }

  return (
    <Form onSubmit={submit}>
        <FormGroup row>
            <Label
            for="name"
            sm={2}
            >
            Nombre
            </Label>
            <Col sm={10}>
            <Input
                id="name"
                name="name"
                placeholder="Ingrese el nombre de la rutina"
                type="name"
            />
            </Col>
        </FormGroup>
        <FormGroup row>
            <Label
            for="grupo"
            sm={2}
            >
            Grupo muscular
            </Label>
            <Col sm={10}>
            <Input
                id="grupo"
                name="grupo"
                placeholder="Indique el grupo muscular que pertenece"
                type="grupo"
            />
            </Col>
        </FormGroup>
        <FormGroup
            check
            row
        >
            <Col
            sm={{
                offset: 2,
                size: 10
            }}
            >
            <Button color="primary" onClick={toggle}>
                Guardar
            </Button>{' '}
            <Button color="secondary" onClick={toggle}>
                Cancelar
            </Button>
            </Col>
        </FormGroup>
        </Form>
  );
}
