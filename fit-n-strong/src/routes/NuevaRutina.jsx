import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Col, Input, FormText } from 'reactstrap';
import axios from 'axios';

export default function NuevaRutina(props) {

    const [routineName, setRoutineName] = useState('');
    const [grupo, setGrupo] = useState('');

    function submit(event) {
        event.preventDefault();
        console.log("Se mandó");
        console.log(routineName, " - ", grupo);
        axios.post('http://20.226.52.146:8080/rutinas', {
            // nombre: routineName,
            // grupo_muscular: grupo
            headers: {
                "Content-Type": "text/plain",
            },
            nombre: routineName,
            grupo_muscular: grupo
        })
        .then(response => console.log(response))
        .then(data => {
            if(data.status === 201) {
                alert("Rutina creada con éxito");
            }
        })
        .catch(error => {
            alert("Ocurrió el siguiente error al tratar de crear la rutina:", error);
        });

        // props.toggle();
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
                value={routineName}
                onChange={(e) => {
                  setRoutineName(e.target.value);
                }}
            />
            </Col>
        </FormGroup>
        <FormGroup row>
            <Label
            for="name"
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
                value={grupo}
                onChange={(e) => {
                  setGrupo(e.target.value);
                }}
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
            <Button color="primary" type='submit'>
                Crear Rutina
            </Button>{' '}
            <Button color="secondary" onClick={props.toggle}>
                Cancelar
            </Button>
            </Col>
        </FormGroup>
        </Form>
  );
}
