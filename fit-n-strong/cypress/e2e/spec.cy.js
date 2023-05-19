/* global cy*/

describe('test cases 1', () => {
  it('Crear rutina - UC01 Done', () => {
      cy.visit('http://localhost:3000')
      cy.contains('Bienvenido a Fit and Strong')
      cy.contains('Mis Rutinas').click()
      cy.contains('Nueva Rutina').click()
      cy.get('#name').type('rutina testing')
      cy.get('#grupo').type('testing')
      cy.get('.btn-primary').click()
    })

  it('Ver rutina - UC04 Done', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Bienvenido a Fit and Strong')
    cy.contains('Mis Rutinas').click()
    cy.get('td:last .btn-success').click()
  })

  it('Editar rutina - UC02 Done', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Bienvenido a Fit and Strong')
    cy.contains('Mis Rutinas').click()
    cy.get('td:last .btn-warning').click()
    cy.wait(10)
    cy.get('#name').type('rutina actualizada')
    cy.get('#grupo').type('grupo actualizado')
    cy.get('.btn-primary').click()
  })

  it('Añadir ejercicio - UC05 Done', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Bienvenido a Fit and Strong')
    cy.contains('Mis Rutinas').click()
    cy.get('td:last .btn-success').click()
    cy.contains('Agregar Ejercicio').click()
    cy.get('#name').type('nombre ejercicio testing')
    cy.get('#reps').type('2')
    cy.get('#duration').type('100[testing seg]')
    cy.get('#peso').type('20')
    cy.get('.btn-primary').click()
  })

  it('Editar ejercicio - UC07 Done', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Bienvenido a Fit and Strong')
    cy.contains('Mis Rutinas').click()
    cy.get('td:last .btn-success').click()
    cy.contains('Agregar Ejercicio')
    cy.get('td:last .btn-warning').click()
    cy.wait(10)
    cy.get('#name').type('nombre ejercicio testing editado')
    cy.get('#reps').type('2')
    cy.get('#duration').type('3 series')
    cy.get('#peso').type('20')
    cy.get('.btn-primary').click()
  })

  it('Borrar ejercicio - UC06 Done', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Bienvenido a Fit and Strong')
    cy.contains('Mis Rutinas').click()
    cy.get('td:last .btn-success').click()
    cy.contains('Agregar Ejercicio')
    cy.get('td:last .btn-danger').click()
    cy.wait(10)
    cy.get('.modal-footer .btn-danger').click()
  })

  it('Borrar rutina - UC03 Done', () => {
    cy.visit('http://localhost:3000')
    cy.contains('Bienvenido a Fit and Strong')
    cy.contains('Mis Rutinas').click()
    cy.get('td:last .btn-danger').click()
    cy.wait(10)
    cy.get('.btn-danger').click()
  })
})

