import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Col, Input } from 'reactstrap';

export default function EditarRutina(props) {

    // hacer llamada a la API para obtener los datos de la rutina que se está modificando

  return (
    <Form>
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
            <Button color="primary" onClick={props.toggle}>
                Guardar
            </Button>{' '}
            <Button color="secondary" onClick={props.toggle}>
                Cancelar
            </Button>
            </Col>
        </FormGroup>
        </Form>
  );
}
