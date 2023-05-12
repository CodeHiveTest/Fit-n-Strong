import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Col, Input, FormText } from 'reactstrap';

export default function NuevaRutina(props) {

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
