import React, { useState } from 'react';
import { Button, Form, FormGroup, Label, Col, Input } from 'reactstrap';

export default function EditarEjercicio(props) {

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
                placeholder="Ingrese el nombre del ejercicio"
                type="name"
            />
            </Col>
        </FormGroup>
        <FormGroup row>
            <Label
            for="reps"
            sm={2}
            >
            Reps.
            </Label>
            <Col sm={10}>
            <Input
                id="reps"
                name="reps"
                type="number"
            />
            </Col>
        </FormGroup>
        <FormGroup row>
            <Label
            for="duration"
            sm={2}
            >
            Duración
            </Label>
            <Col sm={10}>
            <Input
                id="duration"
                name="duration"
                placeholder='Ingrese el tiempo con la unidad de medida'
                type="text"
            />
            </Col>
        </FormGroup>
        <FormGroup row>
            <Label
            for="peso"
            sm={2}
            >
            Peso [kg]
            </Label>
            <Col sm={10}>
            <Input
                id="peso"
                name="peso"
                type="number"
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
                Agregar
            </Button>{' '}
            <Button color="secondary" onClick={props.toggle}>
                Cancelar
            </Button>
            </Col>
        </FormGroup>
        </Form>
  );
}
