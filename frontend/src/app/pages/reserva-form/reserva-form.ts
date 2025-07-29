import { Component } from '@angular/core';
import { ApiService, Reserva } from '../../services/api';

@Component({
  selector: 'app-reserva-form',
  templateUrl: './reserva-form.html',
  styleUrls: ['./reserva-form.scss'],
})
export class ReservaFormComponent {
  reserva: Reserva = {
    nombre_cliente: '',
    correo_cliente: '',
    fecha_reserva: '',
    hora_reserva: '',
    cantidad_personas: 1,
  };

  constructor(private api: ApiService) {}

  guardar() {
    this.api.createReserva(this.reserva).subscribe(() => {
      alert('¡Reserva creada!');
    });
  }
}