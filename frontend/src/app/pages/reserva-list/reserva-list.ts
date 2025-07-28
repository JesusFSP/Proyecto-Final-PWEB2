import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api';

@Component({
  selector: 'app-reserva-list',
  standalone: true,
  imports: [CommonModule],
  template: `
    <h2>Reservas</h2>
    <ul>
      <li *ngFor="let r of reservas">{{ r.id }} - {{ r.fecha }}</li>
    </ul>
  `
})
export class ReservaListComponent implements OnInit {
  reservas: any[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getReservas().subscribe(data => this.reservas = data);
  }
}