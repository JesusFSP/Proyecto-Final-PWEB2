import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { MatListModule } from '@angular/material/list';
import { ApiService } from '../services/api.service';

@Component({
  selector: 'app-reserva-list',
  standalone: true,
  imports: [CommonModule, MatListModule],
  template: `
    <h2 class="mb-3">Reservas (Angular + Material)</h2>
    <mat-list>
      <mat-list-item *ngFor="let r of reservas">
        {{ r.id }} – {{ r.fecha }}
      </mat-list-item>
    </mat-list>
  `,
})
export class ReservaListComponent implements OnInit {
  reservas: any[] = [];

  constructor(private api: ApiService) {}

  ngOnInit() {
    this.api.getReservas().subscribe((data) => (this.reservas = data));
  }
}