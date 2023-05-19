import React, { useEffect, useState } from 'react';
import { Button, Form, FormGroup, Label, Col, Input, FormText } from 'reactstrap';
import axios from 'axios';

export default function AgregarEjercicio({toggle, getExercises, routineId}) {

    const [exerciseName, setExerciseName] = useState('');
    const [reps, setReps] = useState(0);
    const [duration, setDuration] = useState('');
    const [peso, setPeso] = useState(0);

    useEffect(() => {
        getExercises();
    }, []);

    function submit(event) {
        event.preventDefault();
        console.log("Se mandó");
        console.log(exerciseName, " - ", reps);
        axios.post('http://20.226.52.146:8080/ejercicios', {
            headers: {
                "Content-Type": "text/plain",
            },
            nombre: exerciseName,
            repeticiones: reps,
            duracion: duration,
            peso: peso,
            rutina_id: routineId
        })
        .then(response => response.data)
        .then(data => {
            if(data.status === 201) {
                getExercises();
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
                <Label for="name" sm={2}>Nombre</Label>
                <Col sm={10}>
                    <Input
                        id="name"
                        name="name"
                        placeholder="Ingrese el nombre del ejercicio"
                        type="name"
                        value={exerciseName}
                        onChange={(e) => {
                            setExerciseName(e.target.value);
                        }}
                    />
                </Col>
            </FormGroup>
            <FormGroup row>
                <Label for="reps" sm={2}>
                Repeticiones
                </Label>
                <Col sm={10}>
                    <Input
                        id="reps"
                        name="reps"
                        type="number"
                        value={reps}
                        onChange={(e) => {
                            setReps(e.target.value);
                        }}
                    />
                </Col>
            </FormGroup>
            <FormGroup row>
                <Label for="duration" sm={2}>
                Duración
                </Label>
                <Col sm={10}>
                    <Input
                        id="duration"
                        name="duration"
                        placeholder="Indique la duración"
                        type="duration"
                        value={duration}
                        onChange={(e) => {
                            setDuration(e.target.value);
                        }}
                    />
                </Col>
            </FormGroup>
            <FormGroup row>
                <Label for="peso" sm={2}>
                Peso
                </Label>
                <Col sm={10}>
                    <Input
                        id="peso"
                        name="peso"
                        type="number"
                        value={peso}
                        onChange={(e) => {
                            setPeso(e.target.value);
                        }}
                    />
                </Col>
            </FormGroup>
            <FormGroup check row>
                <Col sm={{ offset: 2, size: 10 }}>
                <Button color="primary" type='submit'>
                    Crear Ejercicio
                </Button>{' '}
                <Button color="secondary" onClick={toggle}>
                    Cancelar
                </Button>{' '}
                </Col>
            </FormGroup>
        </Form>
    );
}

