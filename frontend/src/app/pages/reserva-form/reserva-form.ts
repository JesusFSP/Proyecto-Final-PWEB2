import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-reserva-form',
  standalone: true,
  imports: [FormsModule, MatInputModule, MatButtonModule],
  template: `
    <h2>Nueva Reserva</h2>
    <form (ngSubmit)="guardar()">
      <mat-form-field>
        <input matInput placeholder="Fecha" [(ngModel)]="model.fecha" name="fecha" />
      </mat-form-field>
      <br />
      <button mat-raised-button color="primary" type="submit">Guardar</button>
    </form>
  `,
})
export class ReservaFormComponent {
  model = { fecha: '' };

  constructor(private api: ApiService) {}

  guardar() {
    this.api.postReserva(this.model).subscribe(() => {
      alert('Reserva creada');
    });
  }
}